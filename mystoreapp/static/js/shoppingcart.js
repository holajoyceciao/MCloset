window.cart = JSON.parse(sessionStorage.getItem("cart")) || [];

function onSaveChange() {
  sessionStorage.setItem("cart", JSON.stringify(window.cart));
  getSessionProducts("cart");
}

function calSubtotal() {
  let subtotal = window.cart.reduce(
    (acc, item) => parseInt(item["price"]) * parseInt(item["quantity"]) + acc,
    0
  );
  let total_cost = document.getElementById("subtotal");
  total_cost.innerText = subtotal;
}

function updateQuantity(index, quantity) {
  window.cart[index]["quantity"] = quantity;
}

function deleteProducts(index) {
  window.cart.splice(index, 1);
  sessionStorage.setItem("cart", JSON.stringify(window.cart));
  window.location.href = "/cart/";
}
