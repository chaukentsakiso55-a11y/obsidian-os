#[tauri::command]
fn status() -> &'static str { "OBSIDIAN desktop shell ready" }

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![status])
        .run(tauri::generate_context!())
        .expect("error running OBSIDIAN");
}

#[cfg(test)]
mod tests {
    #[test]
    fn status_is_ready() { assert_eq!(super::status(), "OBSIDIAN desktop shell ready"); }
}
