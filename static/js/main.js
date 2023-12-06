document.addEventListener("DOMContentLoaded", function () {

    // Generate lucide icons
    lucide.createIcons();

    // Here we initialize swiper js
    const swiper = new Swiper('.swiper', {
        // Optional parameters
        direction: 'horizontal',
        loop: true,

        autoplay: {
            delay: 5000,
            disableOnInteraction: true,
        },

        // If we need pagination
        pagination: {
            el: '.swiper-pagination',
            dynamicBullets: true,
        },

        // Navigation arrows
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },

        // And if we need a scrollbar
        scrollbar: {
            el: '.swiper-scrollbar',
        },
    });

    // This opens the search bar on mobile screens
    const searchToggleOpen = document.getElementById("mobile-search-open")
    const searchToggleClose = document.getElementById("mobile-search-close")
    const searchBox = document.getElementById("search-box")

    searchToggleOpen.addEventListener("click", () => {
        searchBox.style.display = "flex"
        searchToggleOpen.classList.add("hide")
        searchToggleClose.classList.remove("hide")
    
    })

    // This closes the search bar on mobile screens
    searchToggleClose.addEventListener("click", () => {
        searchBox.style.display = "none"
        searchToggleOpen.classList.remove("hide")
        searchToggleClose.classList.add("hide")
    
    })

    //This opens the sorting menu on click
    const sortToggleOpen = document.getElementById("sort-open")
    const sortLink = document.getElementsByClassName("sort-link")
    const sortBox = document.getElementById("sort-box")

    sortToggleOpen.addEventListener("click", () => {
        sortBox.classList.remove("hide")

    })

    //This hides the navbar on auth pages
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

    // Checks the url for which page we are on and adds the .active class to the link
    let homeUrl = window.location.pathname == "/";
    let shopUrl = window.location.href.includes('shop');
    let contactUrl = window.location.href.includes('contact');
    let cartUrl = window.location.href.includes('cart');
    let profileUrl = window.location.href.includes('users');
    let homeLink = document.getElementById('home')
    let shopLink = document.getElementById('shop')
    let contactLink = document.getElementById('contact')
    let customLink = document.getElementById('custom-shirts')
    let profileLink = document.getElementById('my-profile')
    let cartLink = document.getElementById('cart')
    let cartTotal = document.getElementById('grand-total')

    if (homeUrl) {
        homeLink.classList.add("active");
    } else if (shopUrl) {
        shopLink.classList.add("active");
    } else if (contactUrl) {
        contactLink.classList.add("active");
    } else if (contactUrl) {
        customLink.classList.add("active");
    } else if (profileUrl) {
        profileLink.classList.add("active");
        profileLink.classList.remove("text-light");
    } else if (cartUrl) {
        cartLink.classList.add("active");
        cartLink.classList.remove("text-light");
        cartTotal.classList.add("active");
        cartTotal.classList.remove("text-light");
    }

    //Functionality for the quantity selection element
    let decreaseQuantity = document.getElementsByClassName("decrement-quantity")[0]
    let increaseQuantity = document.getElementsByClassName("increment-quantity")[0]
    let quantityCounter = document.getElementById("quantity-counter")

    increaseQuantity.addEventListener("click", (event) => {
        // increase quantity by one
        event.preventDefault()
        quantityCounter.value = parseInt(quantityCounter.value) + 1;
    });
    
    decreaseQuantity.addEventListener("click", (event) => {
        // decrease quantity by one
        event.preventDefault()
        let currentQuantity = parseInt(quantityCounter.value);
        if (currentQuantity > 1) {
            quantityCounter.value = currentQuantity - 1;
        }
    })

    //Updates the item quantites in the cart
    let updateButton = document.getElementById("update-cart")
    let updateForm = document.getElementById("update-form")

    updateButton.addEventListener("click", () => {
        updateForm.submit()
    })

    //Deletes an item from the cart
    let deleteButton = document.getElementById("update-cart")

    deleteButton.addEventListener("click", () => {
        let csrfToken = "{{ csrf_token }}";
        let itemId = $(this).attr('id').split('remove_')[1];
        let url = `/cart/remove/${itemId}`;
        let data = {'csrfmiddlewaretoken': csrfToken};
    })

})
