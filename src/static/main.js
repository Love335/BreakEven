async function getDeck() {
    let response = await fetch("/api/newdeck");
    let data = await response.json();
    
    document.getElementById("output").textContent =
        JSON.stringify(data, null, 2);
}