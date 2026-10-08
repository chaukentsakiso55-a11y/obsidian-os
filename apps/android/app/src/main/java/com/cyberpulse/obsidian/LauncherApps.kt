package com.cyberpulse.obsidian

import android.content.Context
import android.content.Intent
import android.content.pm.PackageManager

data class LaunchableApp(val label: String, val packageName: String, val activityName: String)

object LauncherApps {
    fun list(context: Context): List<LaunchableApp> {
        val intent = Intent(Intent.ACTION_MAIN).addCategory(Intent.CATEGORY_LAUNCHER)
        val matches = context.packageManager.queryIntentActivities(intent, PackageManager.MATCH_ALL)
        return matches.map {
            LaunchableApp(it.loadLabel(context.packageManager).toString(), it.activityInfo.packageName, it.activityInfo.name)
        }.distinctBy { it.packageName to it.activityName }.sortedBy { it.label.lowercase() }
    }

    fun open(context: Context, app: LaunchableApp) {
        val intent = Intent(Intent.ACTION_MAIN).addCategory(Intent.CATEGORY_LAUNCHER)
            .setClassName(app.packageName, app.activityName)
            .addFlags(Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_ACTIVITY_RESET_TASK_IF_NEEDED)
        context.startActivity(intent)
    }
}
