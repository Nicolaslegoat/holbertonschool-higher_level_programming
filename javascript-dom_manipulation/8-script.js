document.addEventListener('DOMContentLoaded', function () {
    const helloelement = document.querySelector("#hello");
  
    fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => response.json())
      .then(data => {
        helloelement.textContent = data.hello;
      })
      .catch(error => {
        console.error('Error fetching translation:', error);
      });
  });