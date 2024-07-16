document.addEventListener('DOMContentLoaded', (event) => {
    // Função para verificar se todos os valores são zero
    function checkAllZero() {
        const sizeNumberElements = document.querySelectorAll('.size-number');
        let allZero = true;
        sizeNumberElements.forEach(element => {
            if (parseInt(element.textContent, 10) !== 0) {
                allZero = false;
            }
        });
        return allZero;
    }

    // Função para incrementar o valor
    function incrementValue(event) {
        const button = event.target;
        const sizeNumberElement = button.parentElement.querySelector('.size-number');
        let currentValue = parseInt(sizeNumberElement.textContent, 10);
        sizeNumberElement.textContent = currentValue + 1;

        let gradeButton = document.getElementById("gradeButton");
        if (currentValue===0) {
            console.log(currentValue);
            gradeButton.style.backgroundColor = "green";
        }
    
    }

    // Função para decrementar o valor
    function decrementValue(event) {
        let gradeButton = document.getElementById("gradeButton");
        const button = event.target;
        const sizeNumberElement = button.parentElement.querySelector('.size-number');
        let currentValue = parseInt(sizeNumberElement.textContent, 10);
        if (currentValue > 0) {
            sizeNumberElement.textContent = currentValue - 1;
        }
        if (checkAllZero()) {
            gradeButton.style.backgroundColor = "red";}
    }

    // Função para coletar os valores e enviá-los
    function saveChanges() {
        let values = {};
        const boxes = document.querySelectorAll('.box');
        boxes.forEach(box => {
            const sizeNumberElement = box.querySelector('.size-number');
            let sizeValue = parseInt(sizeNumberElement.textContent, 10);
            if (sizeValue > 0) {
                let boxId = box.id;
                values[boxId] = sizeValue;
            }
        });
        localStorage.setItem("grade",JSON.stringify(values));
        document.getElementById("closeModal").click()

        
 
    }


    const addButtons = document.querySelectorAll('.btn-add');
    addButtons.forEach(button => {
        button.addEventListener('click', incrementValue);
    });

    const removeButtons = document.querySelectorAll('.btn-remove');
    removeButtons.forEach(button => {
        button.addEventListener('click', decrementValue);
    });

    const saveButton = document.getElementById('saveChanges');
    saveButton.addEventListener('click', saveChanges);
});


function resetValues() {
    const sizeNumberElements = document.querySelectorAll('.size-number');
    sizeNumberElements.forEach(element => {
        element.textContent = '0';
    });
}

function formData() {
    const gradeData = JSON.parse(localStorage.getItem("grade")) || {};
    const gradeForm = document.getElementById("id_size");
    gradeForm.value = JSON.stringify(gradeData);
    document.getElementById("produtoForm").submit();
}