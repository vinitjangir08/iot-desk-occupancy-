async function refreshStatus() {
  let box = document.getElementById("status-box");
  box.innerHTML = "Updating...";
  
  let res = await fetch("/status");
  let data = await res.json();
  
  box.innerHTML = data.desk;
  
  if (data.desk === "Occupied") {
    box.style.background = "red";
  } else {
    box.style.background = "green";
  }
}
