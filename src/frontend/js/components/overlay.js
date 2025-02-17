export function showLoadingOverlay() {
    const overlay = document.getElementById("loadingOverlay");
    overlay.classList.remove("hidden");
  }
  
export function hideLoadingOverlay() {
    const overlay = document.getElementById("loadingOverlay");
    overlay.classList.add("hidden");
  }