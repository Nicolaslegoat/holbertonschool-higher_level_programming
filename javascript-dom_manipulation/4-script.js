document.addEventListener('DOMContentLoaded', function () {
    const additem = document.querySelector("#add_item");
    const mylist = document.querySelector('.my_list');

    additem.addEventListener('click', function () {
        const newitem = document.createElement('li');
        newitem.textContent = 'Item';
        mylist.appendChild(newitem);
    });
});