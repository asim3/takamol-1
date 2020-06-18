function chack_add_response(response, element) {
  if (response.status === 200) {
    element.innerHTML = "Added";
    element.className = "btn btn-success";
    element.onclick = "";
  } else {
    element.innerHTML = "Add to Favorite";
  }
}

function add_to_favorite(element, form_data) {
  element.innerHTML = "<span class='spinner-border spinner-border-sm'></span>";
  fetch("/accounts/favorite/new/", {
    method: "POST",
    headers: {
      "X-CSRFToken": getCookie("csrftoken"),
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body:
      "title=" +
      form_data.title +
      "&author=" +
      form_data.author +
      "&description=" +
      form_data.description +
      "&url=" +
      form_data.url +
      "&urlToImage=" +
      form_data.urlToImage +
      "&publishedAt=" +
      form_data.publishedAt,
  }).then((response) => chack_add_response(response, element));
}

function chack_delete_response(response, element, article) {
  if (response.status === 200) {
    document.getElementById("article_" + article).remove();
    element.remove();
  } else {
    element.innerHTML = "Delete";
  }
}

function delete_from_favorite(element, pk, article) {
  element.innerHTML = "<span class='spinner-border spinner-border-sm'></span>";
  fetch("/accounts/favorite/delete/" + pk, {
    method: "POST",
    headers: {
      "X-CSRFToken": getCookie("csrftoken"),
    },
  }).then((response) => chack_delete_response(response, element, article));
}

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    var cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
