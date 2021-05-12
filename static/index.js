function handleSubmit(e) {
  e.preventDefault();
  let inputValue = document.querySelector("#input-value").value;
  console.log(inputValue);
}
let form = document.querySelector("#url-form");
form.addEventListener("submit", handleSubmit);

