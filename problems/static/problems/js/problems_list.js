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
    const checkboxes = document.querySelectorAll('input[id=problemCheckbox]');
    const storage = JSON.parse(localStorage.getItem(cartName)) || [];
    checkboxes.forEach((checkbox) => {
        // check input if name in storage
        checkbox.checked = storage.some((item) => parseInt(item) === parseInt(checkbox.value));
    })
}

function setCart() {
    const cart = document.querySelector('.cart');
    cart.innerHTML = "";

    const storage = JSON.parse(localStorage.getItem(cartName)) || [];
    storage.forEach((item) => {
        const li = document.createElement('li');
        const name = document.createElement('p');
        name.innerText = item;

        cart.append(li);
        li.append(name);
    })

}

synchronizeCheckboxes();
setCart();