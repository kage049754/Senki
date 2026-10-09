package com.senki.game

import android.app.Activity
import android.os.Bundle
import android.graphics.Canvas
import android.graphics.Color
import android.graphics.Paint
import android.graphics.RectF
import android.view.MotionEvent
import android.view.View
import kotlin.math.abs
import kotlin.math.max
import kotlin.math.min

class MainActivity : Activity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        window.decorView.systemUiVisibility = 5894 or 1024 or 512 or 4096
        setContentView(SenkiView(this))
    }
}

data class Fighter(val id: String, val name: String, val color: Int, val hp: Float, val attack: Float, val speed: Float, val skill: String)

object FighterRegistry {
    // Add definitions here; selection cards are generated dynamically from this catalog.
    val fighters = listOf(
        Fighter("leaf_runner", "LEAF RUNNER", Color.rgb(80,210,145), 120f, 13f, 210f, "SHADOW DASH"),
        Fighter("ember_guard", "EMBER GUARD", Color.rgb(255,125,85), 155f, 18f, 155f, "FLAME BURST"),
        Fighter("storm_scout", "STORM SCOUT", Color.rgb(100,175,255), 95f, 10f, 260f, "THUNDER SHOT"),
        Fighter("moon_medic", "MOON MEDIC", Color.rgb(210,150,255), 110f, 9f, 190f, "HEAL PULSE")
    )
}

class SenkiView(context: android.content.Context) : View(context) {
    private val p = Paint(Paint.ANTI_ALIAS_FLAG)
    private enum class Screen { MENU, SELECT, BATTLE, RESULT }
    private var screen = Screen.MENU
    private var chosen = 0
    private val fighter get() = FighterRegistry.fighters[chosen]
    private var px = 0f
    private var ex = 0f
    private var php = 100f
    private var ehp = 100f
    private var attackCd = 0f
    private var skillCd = 0f
    private var enemyCd = 0f
    private var spawnCd = 0f
    private var level = 1
    private var xp = 0f
    private var paused = false
    private var won = false
    private var last = 0L
    private var toast = "READY"
    private data class Minion(var x: Float, val ally: Boolean, var hp: Float = 30f, var cd: Float = 0f)
    private val minions = mutableListOf<Minion>()

    override fun onDraw(c: Canvas) {
        super.onDraw(c)
        val w = width.toFloat().coerceAtLeast(1f); val h = height.toFloat().coerceAtLeast(1f)
        when(screen) {
            Screen.MENU -> menu(c,w,h)
            Screen.SELECT -> select(c,w,h)
            Screen.BATTLE -> battle(c,w,h)
            Screen.RESULT -> result(c,w,h)
        }
        if(screen == Screen.BATTLE && !paused) {
            val now = System.currentTimeMillis()
            val dt = if(last == 0L) .016f else ((now-last)/1000f).coerceIn(0f,.05f)
            last=now; update(dt,w)
            postInvalidateDelayed(16)
        } else last=0L
    }

    private fun base(c:Canvas,w:Float,h:Float) {
        c.drawColor(Color.rgb(13,24,29)); p.color=Color.rgb(20,38,42); c.drawRect(0f,0f,w,h*.68f,p)
        p.color=Color.rgb(25,48,48)
        for(i in 0..7) c.drawRect(w*i/7f, h*.15f, w*i/7f+w*.006f, h*.68f,p)
        p.color=Color.rgb(30,58,52); c.drawRect(0f,h*.68f,w,h,p)
        p.color=Color.rgb(42,78,62); c.drawRect(0f,h*.66f,w,h*.70f,p)
    }
    private fun menu(c:Canvas,w:Float,h:Float) {
        base(c,w,h); txt(c,"SENKI",w*.09f,h*.32f,h*.16f,Color.WHITE,true)
        txt(c,"OFFLINE LANE BATTLE",w*.095f,h*.41f,h*.035f,Color.rgb(94,221,163),true)
        txt(c,"A new battle begins here.",w*.095f,h*.49f,h*.028f,Color.LTGRAY,false)
        btn(c,RectF(w*.65f,h*.30f,w*.91f,h*.46f),"PLAY",Color.rgb(46,190,126),h)
        btn(c,RectF(w*.65f,h*.51f,w*.91f,h*.67f),"CHARACTERS",Color.rgb(49,66,78),h)
        txt(c,"EARLY PROTOTYPE • LANDSCAPE",w*.095f,h*.90f,h*.022f,Color.GRAY,true)
    }
    private fun select(c:Canvas,w:Float,h:Float) {
        base(c,w,h); txt(c,"SELECT YOUR FIGHTER",w*.05f,h*.12f,h*.065f,Color.WHITE,true)
        txt(c,"STARTER ROSTER • "+FighterRegistry.fighters.size+" REGISTERED",w*.05f,h*.18f,h*.027f,Color.LTGRAY,false)
        val gap=w*.018f; val cardW=(w*.90f-gap*(FighterRegistry.fighters.size-1))/FighterRegistry.fighters.size
        FighterRegistry.fighters.forEachIndexed { i,f ->
            val r=RectF(w*.05f+i*(cardW+gap),h*.25f,w*.05f+i*(cardW+gap)+cardW,h*.73f)
            box(c,r,if(i==chosen) f.color else Color.rgb(35,49,55),h*.025f)
            circle(c,r.centerX(),r.top+h*.16f,h*.055f,f.color)
            center(c,f.name,r.centerX(),r.top+h*.29f,h*.029f,Color.WHITE,true)
            center(c,"HP "+f.hp.toInt()+" / ATK "+f.attack.toInt(),r.centerX(),r.top+h*.38f,h*.022f,Color.LTGRAY,false)
            center(c,f.skill,r.centerX(),r.top+h*.45f,h*.023f,Color.WHITE,true)
            if(i==chosen) center(c,"SELECTED",r.centerX(),r.bottom-h*.05f,h*.023f,Color.WHITE,true)
        }
        btn(c,RectF(w*.05f,h*.80f,w*.22f,h*.91f),"BACK",Color.rgb(49,66,78),h)
        btn(c,RectF(w*.72f,h*.80f,w*.95f,h*.91f),"START BATTLE",Color.rgb(46,190,126),h)
    }
    private fun battle(c:Canvas,w:Float,h:Float) {
        base(c,w,h); txt(c,"MATCH 01 • LV "+level+" • XP "+xp.toInt()+"/100",w*.03f,h*.07f,h*.03f,Color.WHITE,true)
        bar(c,w*.03f,h*.14f,w*.28f,h*.05f,php/fighter.hp,"YOU",h)
        bar(c,w*.69f,h*.14f,w*.28f,h*.05f,ehp/100f,"RIVAL",h)
        tower(c,w*.06f,h*.50f,true,h); tower(c,w*.94f,h*.50f,false,h)
        hero(c,px,h*.60f,fighter.color,"YOU",h); hero(c,ex,h*.60f,Color.rgb(240,103,104),"CPU",h)
        minions.forEach { m -> circle(c,m.x,h*.65f,h*.018f,if(m.ally) Color.GREEN else Color.RED) }
        btn(c,RectF(w*.02f,h*.79f,w*.12f,h*.92f),"MENU",Color.rgb(49,66,78),h)
        btn(c,RectF(w*.14f,h*.79f,w*.26f,h*.92f),if(paused) "RESUME" else "PAUSE",Color.rgb(49,66,78),h)
        btn(c,RectF(w*.29f,h*.80f,w*.43f,h*.92f),"◀ MOVE",Color.rgb(49,66,78),h)
        btn(c,RectF(w*.45f,h*.80f,w*.59f,h*.92f),"MOVE ▶",Color.rgb(49,66,78),h)
        btn(c,RectF(w*.63f,h*.79f,w*.78f,h*.93f),"ATTACK",Color.rgb(58,111,150),h)
        btn(c,RectF(w*.80f,h*.79f,w*.98f,h*.93f),fighter.skill,fighter.color,h)
        txt(c,toast,w*.34f,h*.07f,h*.025f,Color.rgb(245,220,127),true)
        if(paused) { box(c,RectF(w*.37f,h*.32f,w*.63f,h*.62f),Color.rgb(18,29,31),h*.025f); center(c,"PAUSED",w*.5f,h*.44f,h*.065f,Color.WHITE,true) }
    }
    private fun result(c:Canvas,w:Float,h:Float) {
        base(c,w,h); center(c,if(won) "VICTORY" else "DEFEAT",w/2,h*.35f,h*.13f,if(won) Color.GREEN else Color.RED,true)
        center(c,if(won) "Rival defeated!" else "Try again!",w/2,h*.45f,h*.035f,Color.WHITE,false)
        btn(c,RectF(w*.20f,h*.62f,w*.43f,h*.78f),"REMATCH",Color.rgb(46,190,126),h)
        btn(c,RectF(w*.57f,h*.62f,w*.80f,h*.78f),"MAIN MENU",Color.rgb(49,66,78),h)
    }
    private fun update(dt:Float,w:Float) {
        attackCd=max(0f,attackCd-dt); skillCd=max(0f,skillCd-dt); enemyCd=max(0f,enemyCd-dt); spawnCd-=dt
        if(spawnCd<=0f) { minions.add(Minion(w*.12f,true)); minions.add(Minion(w*.88f,false)); spawnCd=5f }
        minions.forEach { m ->
            m.cd=max(0f,m.cd-dt); m.x+=(if(m.ally) 1 else -1)*w*.045f*dt
            if(m.cd<=0f && abs(m.x-w*.5f)<w*.07f) { m.cd=1.4f; if(m.ally) ehp-=1f else php-=1f }
        }
        minions.removeAll { it.x<0f || it.x>w }
        if(ex>px+w*.1f) ex-=fighter.speed*.3f*dt else if(ex<px-w*.1f) ex+=fighter.speed*.3f*dt
        if(enemyCd<=0f && abs(ex-px)<w*.17f) { enemyCd=1.1f; php-=5f; toast="RIVAL STRIKES" }
        php=php.coerceIn(0f,fighter.hp); ehp=ehp.coerceIn(0f,100f); px=px.coerceIn(w*.12f,w*.86f); ex=ex.coerceIn(w*.12f,w*.88f)
        if(php<=0f || ehp<=0f) { won=ehp<=0f; xp+=(if(won) 45f else 15f); if(xp>=100f) { level++; xp-=100f }; screen=Screen.RESULT }
    }
    private fun reset() { screen=Screen.BATTLE; px=width*.24f; ex=width*.75f; php=fighter.hp; ehp=100f; attackCd=0f; skillCd=0f; enemyCd=0f; spawnCd=1f; paused=false; minions.clear(); toast="FIGHT!"; invalidate() }
    private fun attack() { if(paused||attackCd>0f)return; attackCd=.55f; if(abs(ex-px)<width*.24f) { ehp-=fighter.attack; toast="HIT! -" + fighter.attack.toInt()+" HP" } else toast="TOO FAR"; invalidate() }
    private fun skill() { if(paused||skillCd>0f)return; skillCd=4f; if(abs(ex-px)<width*.55f) { ehp-=fighter.attack*2.4f; php=min(fighter.hp,php+8f); toast=fighter.skill+"!"; } else toast="OUT OF RANGE"; invalidate() }
    override fun onTouchEvent(e:MotionEvent):Boolean {
        if(e.action!=MotionEvent.ACTION_UP)return true
        val x=e.x; val y=e.y; val w=width.toFloat(); val h=height.toFloat()
        when(screen) {
            Screen.MENU -> { if(hit(x,y,w*.6f,h*.25f,w,h*.7f)) screen=Screen.SELECT }
            Screen.SELECT -> {
                if(y in (h*.22f)..(h*.76f)) { val gap=w*.018f; val cw=(w*.9f-gap*(FighterRegistry.fighters.size-1))/FighterRegistry.fighters.size; val i=((x-w*.05f)/(cw+gap)).toInt(); if(i in FighterRegistry.fighters.indices) chosen=i }
                else if(hit(x,y,0f,h*.78f,w*.25f,h)) screen=Screen.MENU
                else if(hit(x,y,w*.68f,h*.78f,w,h)) reset()
            }
            Screen.BATTLE -> {
                if(hit(x,y,0f,h*.76f,w*.13f,h)) screen=Screen.MENU
                else if(hit(x,y,w*.13f,h*.76f,w*.28f,h)) paused=!paused
                else if(!paused && hit(x,y,w*.60f,h*.76f,w*.80f,h)) attack()
                else if(!paused && hit(x,y,w*.79f,h*.76f,w,h)) skill()
                else if(!paused && hit(x,y,w*.27f,h*.76f,w*.45f,h)) px=max(w*.12f,px-fighter.speed*.2f)
                else if(!paused && hit(x,y,w*.45f,h*.76f,w*.61f,h)) px=min(w*.86f,px+fighter.speed*.2f)
            }
            Screen.RESULT -> { if(hit(x,y,w*.16f,h*.58f,w*.46f,h*.8f)) reset() else if(hit(x,y,w*.54f,h*.58f,w*.84f,h*.8f)) screen=Screen.MENU }
        }
        invalidate(); return true
    }
    private fun hit(x:Float,y:Float,l:Float,t:Float,r:Float,b:Float)=x>=l&&x<=r&&y>=t&&y<=b
    private fun box(c:Canvas,r:RectF,color:Int,rad:Float) { p.color=color; c.drawRoundRect(r,rad,rad,p) }
    private fun circle(c:Canvas,x:Float,y:Float,r:Float,color:Int) { p.color=color; c.drawCircle(x,y,r,p) }
    private fun txt(c:Canvas,s:String,x:Float,y:Float,size:Float,color:Int,bold:Boolean) { p.color=color; p.textSize=size; p.typeface=if(bold) android.graphics.Typeface.DEFAULT_BOLD else android.graphics.Typeface.DEFAULT; c.drawText(s,x,y,p) }
    private fun center(c:Canvas,s:String,x:Float,y:Float,size:Float,color:Int,bold:Boolean) { p.textSize=size; p.typeface=if(bold) android.graphics.Typeface.DEFAULT_BOLD else android.graphics.Typeface.DEFAULT; txt(c,s,x-p.measureText(s)/2f,y,size,color,bold) }
    private fun btn(c:Canvas,r:RectF,s:String,color:Int,h:Float) { box(c,r,color,h*.025f); center(c,s,r.centerX(),r.centerY()+h*.01f,h*.027f,Color.WHITE,true) }
    private fun bar(c:Canvas,x:Float,y:Float,w:Float,h:Float,f:Float,label:String,screenH:Float) { txt(c,label,x,y-screenH*.012f,screenH*.022f,Color.WHITE,true); box(c,RectF(x,y+screenH*.005f,x+w,y+screenH*.005f+h),Color.DKGRAY,h/3); box(c,RectF(x,y+screenH*.005f,x+w*f.coerceIn(0f,1f),y+screenH*.005f+h),if(f>.3f) Color.rgb(83,220,148) else Color.RED,h/3) }
    private fun hero(c:Canvas,x:Float,y:Float,color:Int,label:String,h:Float) { circle(c,x,y-h*.08f,h*.035f,color); box(c,RectF(x-h*.035f,y-h*.045f,x+h*.035f,y+h*.035f),color,h*.014f); center(c,label,x,y+h*.10f,h*.02f,Color.WHITE,true) }
    private fun tower(c:Canvas,x:Float,y:Float,ally:Boolean,h:Float) { val col=if(ally) Color.rgb(77,174,136) else Color.rgb(207,91,91); box(c,RectF(x-h*.035f,y-h*.14f,x+h*.035f,y+h*.1f),col,h*.012f); center(c,if(ally) "ALLY BASE" else "RIVAL BASE",x,y+h*.14f,h*.019f,Color.WHITE,true) }
}
