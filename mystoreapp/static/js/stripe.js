async function createCheckoutSession() {
  let cartItem = JSON.parse(sessionStorage.getItem("cart")) || [];

  try {
    const response = await fetch("/checkout/create-checkout-session", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        request: cartItem,
      }),
    });

    if (!response.ok) {
      throw new Error("Failed to create checkout session.");
    }
    const result = await response.json();
    const stripe = Stripe(
      "pk_test_51NHybZFtRmC6GWxQE7E8vVeO32laNHkrJsgLp0tcFAlalhBZYfnRkfIVD2zXulfUpviMJvRHGCHMYk84W1ZJQOaV00x9RAxmnV"
    );

    return stripe.redirectToCheckout({ sessionId: result.sessionId });
  } catch (error) {
    console.error(error);
    // Handle the error appropriately (e.g., show an error message)
  }
}
