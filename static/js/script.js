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
const formPopup = document.querySelector('.login-popup');
const closePopupBtn = document.querySelector('.login-popup .close-btn');
const loginSignUpLink = document.querySelectorAll('.login-form .bottom-link a');
 
showPopupBtns.forEach(btn => {                        // Show Popup
    btn.addEventListener('click', () => {
        document.body.classList.add('show-popup');
    });
});

closePopupBtn.addEventListener('click', () => {       // Close Popup
    document.body.classList.remove('show-popup');
});

loginSignUpLink.forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        formPopup.classList[link.id =="signup-link" ? 'add' : 'remove']('show-signup');
    });
});
