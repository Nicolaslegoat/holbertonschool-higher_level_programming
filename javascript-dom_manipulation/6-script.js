document.addEventListener('DOMContentLoaded', function () {
    const characterelement = document.querySelector("#character");
  
    fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
      .then(response => response.json())
      .then(data => {
        characterelement.textContent = data.name;
      })
      .catch(error => {
        console.error('Error fetching character:', error);
      });
  });