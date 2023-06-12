function updateItemCount(page = "cart") {
  let cart = JSON.parse(sessionStorage.getItem("cart")) || [];

  let itemCount = 0;
  for (let i = 0; i < cart.length; i++) {
    itemCount += parseInt(cart[i].quantity);
  }

  document.getElementById("cart_count").innerText = " " + itemCount;
  document.getElementById("cart_count_mobile").innerText = " " + itemCount;
  if (page === "cart") {
    document.getElementById("total_count").innerText = itemCount + " ";
  } else if (page === "checkout") {
    document.getElementById("total_count").innerText = itemCount + " ";
  }
}

function getSessionProducts(page) {
  if (sessionStorage.getItem("cart") !== null) {
    let cart = encodeURIComponent(sessionStorage.getItem("cart"));
    let url = `/${page}/?cart=${cart}`;

    if (page === "checkout") {
      let success = new URLSearchParams(window.location.search).get("success");
      if (success === "true") {
        sessionStorage.removeItem("cart");
        alert("Order Received!");
        window.location.href = "/";
        return;
      }
    }

    if (!window.location.href.includes(url)) {
      window.location.href = url;
    }
  }
}
