document.addEventListener('DOMContentLoaded',()=>{
    const art2= document.getElementById('art2');
    const formHtml=`
    <div>
        <input id="tareaInput" placeholder="Escribo una idea..."/>
        <button id="addBtn">Agregar</button>
    </div>
    <ul id="lista"></ul>
    `;
    art2.insertAdjacentElement('beforeend',formHtml);

    const input= document.getElementById('tareaInput');
    const btn= document.getElementById('addBtn');
    const lista= document.getElementById('lista');

    addbtn.addEventListener('click',()=>{
        const val= input.value.trim();
        if (!val) return alert('Ver una serie')
        const li = document.createElement('li');
        li.innerText= val;
        lista.appendChild(li);
        input.value='';
});
});