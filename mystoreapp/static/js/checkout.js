let cart = JSON.parse(sessionStorage.getItem("cart")) || [];

function fillCartField() {
  if (cart.length) {
    let cartField = document.getElementById("checkout-cart");
    cartField.value = JSON.stringify(cart);
  }
}

function calSubtotal() {
  if (cart !== null && cart.length) {
    let subtotal = cart.reduce(
      (acc, item) => parseInt(item["price"]) * parseInt(item["quantity"]) + acc,
      0
    );
    let total_cost = document.getElementById("subtotal");
    total_cost.innerText = subtotal;
  }
}

window.onload = function () {
  setTimeout(function () {
    fillCartField();
  }, 1000);
};
