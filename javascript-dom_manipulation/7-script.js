document.addEventListener('DOMContentLoaded', function () {
    const listmovie = document.querySelector("#list_movies");
  
    fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => response.json())
      .then(data => {
        data.results.forEach(movie => {
            const listitem = document.createElement('li');
            listitem.textContent = movie.title;
            listmovie.appendChild(listitem);
        });
      })
      .catch(error => {
        console.error('Error fetching movies:', error);
      });
  });