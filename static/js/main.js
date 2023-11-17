/* This snippet is required to render the Lucide Icons -> https://lucide.dev/guide/packages/lucide */
lucide.createIcons();

/* Custom settings for the bootstrap carousel -> https://getbootstrap.com/docs/4.6/components/carousel/ */
$('.carousel').carousel({
    interval: 5000,
    touch: true,
})

/* Checks if the url is one of the login/logout/password urls and hides the header */

document.addEventListener("DOMContentLoaded", function() {
    console.log("Fired!")
    let loginUrl = window.location.href.includes('login');
    let logoutUrl = window.location.href.includes('logout');
    let signupUrl = window.location.href.includes('signup');
    let resetUrl = window.location.href.includes('reset');
    const header = document.getElementById('header')

    if (loginUrl) {
        header.classList.add("hide");
    } else if (logoutUrl) {
        header.classList.add("hide");
    } else if (signupUrl) {
        header.classList.add("hide");
    } else if (resetUrl) {
        header.classList.add("hide");
    }
});
