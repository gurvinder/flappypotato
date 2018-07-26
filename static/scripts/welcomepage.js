document.querySelector("#playbutton").addEventListener('click', () => {
  const url = "/game?username="+ document.querySelector("#username");
  options = {method: "GET", credentials: "same-origin"}
  fetch(new Request(url, options));
});


//   const url = "/todo?listItem="+ value;
//   options = {
//     method: "POST",
//     credentials: "same-origin",
//   }
//   const request = new Request(url, options);
//   fetch(request)
// }");
//   const url = "/todo?listItem="+ value;
//   options = {
//     method: "POST",
//     credentials: "same-origin",
//   }
//   const request = new Request(url, options);
//   fetch(request)
// }