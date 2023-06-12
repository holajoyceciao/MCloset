let totalProducts = window.totalProducts;
let searchItem = window.searchItem;

function onPageSwap(type) {
  let page = new URLSearchParams(window.location.search).get("page") || 1;
  let currentPage = parseInt(page);
  if (type === "p") {
    if (currentPage > 1) {
      let previousPage = currentPage - 1;
      appendPageNumber(previousPage);
      window.location.reload();
    }
  } else {
    if (currentPage * 6 < totalProducts) {
      let nextPage = currentPage + 1;
      appendPageNumber(nextPage);
      window.location.reload();
    }
  }
}

function checkPage() {
  let page = new URLSearchParams(window.location.search).get("page") || 1;
  let currentPage = parseInt(page);

  let previousButton = document.querySelector("#previous-button");
  let nextButton = document.querySelector("#next-button");

  if (currentPage === 1) {
    previousButton.disabled = true;
  }

  if (currentPage * 6 >= totalProducts) {
    nextButton.disabled = true;
  }
}

function appendPageNumber(page) {
  let currentUrl = new URL(window.location.href);
  let params = currentUrl.searchParams;
  params.set("page", page);
  window.history.pushState({}, "", currentUrl.toString());
}

function getSubcategory(subcategoryName, categoryName) {
  categoryName = categoryName || "";
  subcategoryName = subcategoryName || "";

  let currentUrl = new URL(window.location.href);
  let params = currentUrl.searchParams;
  if (currentUrl.search != "") {
    currentUrl.search = "";
  }
  if (subcategoryName != "" && categoryName != "") {
    params.set("category", categoryName);
    params.set("subcategory", subcategoryName);
    window.history.pushState({}, "", currentUrl.toString());
    window.location.reload();
  } else {
    params.delete("category");
    params.delete("subcategory");
    window.history.replaceState({}, "", "/");
    window.location.href = "/";
  }

  if (subcategoryName != null) {
    document.getElementById("categoryName").innerText = subcategoryName;
  }
}

function getTheSection(value) {
  if (value != null) {
    document.getElementById(value).scrollIntoView({ behavior: "smooth" });
  }
}

// Search product
function onSearchChange(value) {
  value = value || "";
  searchItem = value;

  let currentUrl = new URL(window.location.href);
  let params = currentUrl.searchParams;

  if (value) {
    params.set("search", value);
    params.set("page", 1);
    window.history.pushState({}, "", currentUrl.toString());
    window.location.reload();
  } else {
    params.delete("search");
    window.history.replaceState({}, "", "/");
    window.location.href = "/";
  }
}

window.onload = function () {
  if (window.location.pathname === "/") {
    history.replaceState(
      "",
      document.title,
      window.location.pathname + window.location.search
    );
  }

  let currentUrl = new URL(window.location.href);
  let convertToArray = currentUrl.search.split("=");
  let getSubcategory = convertToArray[convertToArray.length - 1];
  if (currentUrl.search != "") {
    document.getElementById("Products").scrollIntoView({ behavior: "smooth" });
  }
  if (currentUrl.search.includes("subcategory") && getSubcategory != null) {
    document.getElementById("categoryName").innerText = getSubcategory;
  } else {
    document.getElementById("categoryName").innerText = "PRODUCTS";
  }
};
