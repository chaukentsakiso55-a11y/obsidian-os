package com.cyberpulse.obsidian

import org.junit.Assert.assertEquals
import org.junit.Test

class LauncherModelTest {
    @Test fun appModelStoresLaunchTarget() {
        val app = LaunchableApp("Browser", "com.example.browser", "com.example.browser.Home")
        assertEquals("Browser", app.label)
        assertEquals("com.example.browser", app.packageName)
    }
}
