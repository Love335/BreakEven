async function getDeck() {
	let response = await fetch("/api/newdeck");
	let data = await response.json();

	document.getElementById("output").textContent =
		JSON.stringify(data, null, 2);
}

document.getElementById("hit-btn").addEventListener("click", () => {
	fetch("/hit", {
		method: "POST",
		headers: {
		}
	})
		.then(res => res.json())
		.then(data => {
			console.log(data);      // whatever your game.hit() returns
		})
});
