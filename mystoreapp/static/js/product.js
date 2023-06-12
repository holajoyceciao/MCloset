function updateItemSpec(type, value) {
  switch (type) {
    case "size":
    case "quantity":
    case "color":
      window.itemSpec[type] = value;
      break;
    default:
      console.error("Invalid type");
  }
}

function onAddItem(product_id, product_name, price) {
  if (
    window.itemSpec["size"] &&
    window.itemSpec["quantity"] &&
    window.itemSpec["color"]
  ) {
    window.itemSpec["product_id"] = product_id;
    window.itemSpec["product_name"] = product_name;
    window.itemSpec["price"] = price;

    let cart =
      sessionStorage.getItem("cart") !== null
        ? JSON.parse(sessionStorage.getItem("cart"))
        : [];

    let found = false;

    for (let i = 0; i < cart.length; i++) {
      if (
        cart[i].product_id === product_id &&
        cart[i].size === window.itemSpec["size"] &&
        cart[i].color === window.itemSpec["color"]
      ) {
        cart[i].quantity =
          parseInt(cart[i].quantity) + parseInt(window.itemSpec["quantity"]);
        found = true;
        break;
      }
    }
    if (!found) {
      cart.push(window.itemSpec);
    }

    sessionStorage.setItem("cart", JSON.stringify(cart));

    updateItemCount();
  }
}
