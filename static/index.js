function handleSubmit(e) {
  e.preventDefault();
  let inputValue = document.querySelector("#input-value").value;
  console.log(inputValue);
  handleInput(inputValue);
}
let form = document.querySelector("#url-form");
form.addEventListener("submit", handleSubmit);



function handleInput(e) {
  // console.log(e.target.value);
}
