function copyTextToClipboard() {
    const elem = document.createElement('textarea');
    elem.value = String.raw`{{ problem.text }}`;
    document.body.appendChild(elem);
    elem.select();
    document.execCommand('copy');
    document.body.removeChild(elem);
}

const cartName = 'problems_cart'

function handleProblemCheckbox(checkbox) {
    const problemId = parseInt(checkbox.value)
    const cart = JSON.parse(localStorage.getItem(cartName)) || [];
    if (checkbox.checked) {
        if (cart.indexOf(problemId) === -1) {
            cart.push(problemId)
        }
    } else {
        if (cart.indexOf(problemId) > -1) {
            cart.splice(cart.indexOf(problemId), 1);
        }
    }
    localStorage.setItem(cartName, JSON.stringify(cart));
    setCart();
}

function synchronizeCheckboxes() {
    const checkboxes = document.querySelectorAll('.problemCheckbox');
    const storage = JSON.parse(localStorage.getItem(cartName)) || [];
    checkboxes.forEach((checkbox) => {
        // check input if name in storage
        checkbox.checked = storage.some((item) => parseInt(item) === parseInt(checkbox.value));
    })
}

function setCart() {
    const cart = document.getElementById('cart');
    const cartCard = document.getElementById('cartCard')
    cart.innerHTML = "";

    const storage = JSON.parse(localStorage.getItem(cartName)) || [];
    if (storage.length > 0) {
        cartCard.style.display = 'block';
        storage.forEach((item) => {
            const li = document.createElement('li');
            li.className = 'list-group-item';
            const problemId = item;
            li.innerHTML = `
                <div class="mt-2 me-2">
                    [<a href="/problem/${problemId}" class="card-link">${problemId}</a>]
                </div> 
            `;
            cart.append(li);
        })
    } else {
        cartCard.style.display = 'none';
    }
}

function clearCart() {
    const cart = [];
    localStorage.setItem(cartName, JSON.stringify(cart));
    synchronizeCheckboxes();
    setCart();
}

synchronizeCheckboxes();
setCart();