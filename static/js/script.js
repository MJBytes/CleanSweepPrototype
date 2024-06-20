// DROP DOWN JS FUNCTIONALITY FOR NAV LINKS
           
const toggleBtn = document.querySelector('.ham-btn'); 
const toggleBtnIcon = document.querySelector('.ham-btn i');
const dropDownMenu = document.querySelector('.dropdown_menu'); 

toggleBtn.onclick = function () {
    dropDownMenu.classList.toggle('open');
    const isOpen = dropDownMenu.classList.contains('open');

    toggleBtnIcon.className = isOpen
        ? 'fa-solid fa-xmark'
        : 'fa-solid fa-bars';
};


// LOGIN POPUP FUNCTIONALITY

const showPopupBtns = document.querySelectorAll('.login-btn');
const closePopupBtn = document.querySelector('.login-popup .close-btn');

 
showPopupBtns.forEach(btn => {                        // Show Popup
    btn.addEventListener('click', () => {
        document.body.classList.add('show-popup');
    });
});

closePopupBtn.addEventListener('click', () => {       // Close Popup
    document.body.classList.remove('show-popup');
});

