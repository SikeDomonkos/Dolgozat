document.addEventListener('DOMContentLoaded', function () {
    // element-one: Dupla kattintásra hozzáad egy "animation" class-t kattintáskor
    document.getElementById('element-one').addEventListener('dblclick', function() {
        this.classList.add('animation');
    });

    // element-two: Ha rámegy az egér, hozzáad egy box-shadow-t
    const elementTwo = document.getElementById('element-two');
        function addBoxShadow() {
            elementTwo.style.boxShadow = '0 4px 8px rgba(0, 0, 0, 0.9)';
        }
        function removeBoxShadow() {
            elementTwo.style.boxShadow = 'none';
        }
        elementTwo.addEventListener('mouseenter', addBoxShadow);
        elementTwo.addEventListener('mouseleave', removeBoxShadow);
    
    // element-three: Kattintásra eltűnik
    document.getElementById('element-three').addEventListener('click', function() {
        this.classList.add('hidden');
    });

    // element-four: Kattintásra a háttere zöld lesz
    document.getElementById('element-four').addEventListener('click', function() {
        document.getElementById('element-four').style.backgroundColor = "green"
    });
});
