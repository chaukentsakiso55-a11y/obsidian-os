package com.cyberpulse.obsidian

import android.app.Activity
import android.app.role.RoleManager
import android.content.Intent
import android.graphics.Color
import android.os.Build
import android.os.Bundle
import android.provider.Settings
import android.view.ViewGroup
import android.widget.*
import android.text.Editable
import android.text.TextWatcher

class MainActivity : Activity() {
    private lateinit var appsView: LinearLayout
    private lateinit var search: EditText
    private fun text(value: String, size: Float) = TextView(this).apply {
        text = value
        textSize = size
        setTextColor(Color.rgb(204, 230, 250))
        setPadding(12, 14, 12, 14)
    }
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val root = LinearLayout(this).apply {
            orientation = LinearLayout.VERTICAL
            setBackgroundColor(Color.rgb(7, 12, 21))
            setPadding(20, 30, 20, 15)
        }
        root.addView(text("◈ OBSIDIAN", 30f).apply { setTextColor(Color.rgb(75, 198, 255)) })
        root.addView(text("ANDROID HYBRID · PRIVATE WORKSPACE", 12f))
        root.addView(text("Your apps. Your control.", 20f))
        fun button(title: String, action: () -> Unit) = Button(this).apply {
            text = title
            setOnClickListener { action() }
        }
        root.addView(button("Security analysis") { startActivity(Intent(this, SecurityActivity::class.java)) })
        root.addView(button("Android Settings") { startActivity(Intent(Settings.ACTION_SETTINGS)) })
        root.addView(button("Set OBSIDIAN as Home") { chooseHome() })
        search = EditText(this).apply {
            hint = "Search installed apps"
            setHintTextColor(Color.LTGRAY)
            setTextColor(Color.WHITE)
            isSingleLine = true
        }
        root.addView(search)
        root.addView(text("APPLICATIONS", 16f))
        appsView = LinearLayout(this).apply { orientation = LinearLayout.VERTICAL }
        val scroll = ScrollView(this).apply { addView(appsView) }
        root.addView(scroll, LinearLayout.LayoutParams(ViewGroup.LayoutParams.MATCH_PARENT, 0, 1f))
        root.addView(text("Android remains installed. You can change Home in Settings.", 12f))
        setContentView(root)
        search.addTextChangedListener(object : TextWatcher {
            override fun beforeTextChanged(s: CharSequence?, start: Int, count: Int, after: Int) {}
            override fun onTextChanged(s: CharSequence?, start: Int, before: Int, count: Int) { showApps(s.toString()) }
            override fun afterTextChanged(s: Editable?) {}
        })
        showApps("")
    }
    override fun onResume() {
        super.onResume()
        if (::appsView.isInitialized) showApps(search.text.toString())
    }
    private fun showApps(query: String) {
        appsView.removeAllViews()
        val apps = LauncherApps.list(this).filter { it.label.contains(query, ignoreCase = true) }
        if (apps.isEmpty()) appsView.addView(text("No matching apps", 14f))
        apps.forEach { app ->
            appsView.addView(Button(this).apply {
                text = app.label
                isAllCaps = false
                setOnClickListener {
                    try { LauncherApps.open(this@MainActivity, app) }
                    catch (_: Exception) { Toast.makeText(this@MainActivity, "Unable to launch", Toast.LENGTH_SHORT).show() }
                }
            })
        }
    }
    private fun chooseHome() {
        if (Build.VERSION.SDK_INT >= 29) {
            val manager = getSystemService(RoleManager::class.java)
            if (manager.isRoleAvailable(RoleManager.ROLE_HOME)) {
                if (!manager.isRoleHeld(RoleManager.ROLE_HOME)) startActivityForResult(manager.createRequestRoleIntent(RoleManager.ROLE_HOME), 10)
                else Toast.makeText(this, "Already selected as Home", Toast.LENGTH_SHORT).show()
                return
            }
        }
        startActivity(Intent(Settings.ACTION_HOME_SETTINGS))
    }
}
