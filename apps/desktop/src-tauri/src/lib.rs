#[tauri::command]
fn status() -> &'static str { "OBSIDIAN desktop shell ready" }

#[tauri::command]
fn platform_info() -> PlatformInfo {
    PlatformInfo {
        os: std::env::consts::OS.to_owned(),
        architecture: std::env::consts::ARCH.to_owned(),
        mode: "hybrid".to_owned(),
    }
}

#[derive(serde::Serialize)]
struct PlatformInfo {
    os: String,
    architecture: String,
    mode: String,
}

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![status, platform_info])
        .run(tauri::generate_context!())
        .expect("error running OBSIDIAN");
}

#[cfg(test)]
mod tests {
    #[test]
    fn status_is_ready() { assert_eq!(super::status(), "OBSIDIAN desktop shell ready"); }
    #[test]
    fn platform_is_hybrid() { assert_eq!(super::platform_info().mode, "hybrid"); }
}
