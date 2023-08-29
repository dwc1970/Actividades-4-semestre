const shopContent = document.getElementById("shopContent");
const cart = []; // Este es nuestro carrito, un array vacio

productos.forEach((producto) => {
    const content = document.createElement("div");
    content.innerHTML = `
        <img src="${producto.img}">
        <h3>${producto.productName}</h3>
        <p>${producto.price} $</p>
    `;
    shopContent.append(content);
});

const buyButton = document.createElement("button");
buyButton.innerText = "comprar";

content.append(buyButton);

buyButton.append(buyButton);

buyButton.addEventListener("click", () => {
    creat.push({
        id: product.id,
        productName: product.productName,
        price: product.price,
        quanty: product.quanty,
        img : product.img,
    })
    console.log(cart)
})