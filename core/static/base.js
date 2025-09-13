
// Home Script
const logo = document.getElementById('logo');

    const originalHTML = 'S|<span style="color:#12f14a">Ex</span>'; // estado normal
    const hoverHTML = 'Simul<span style="color:#12f14a">Ex</span>'; // hover com Ex verde

    // Inicializa com o estado normal
    logo.innerHTML = originalHTML;

    logo.addEventListener('mouseenter', () => {
        logo.innerHTML = hoverHTML; // mostra SimulEx com Ex verde
    });

    logo.addEventListener('mouseleave', () => {
        logo.innerHTML = originalHTML; // volta para S|Ex com Ex verde
    });

// Form Script
const disciplinasSelect = document.getElementById("disciplinas");
    disciplinasSelect.addEventListener("change", function() {
      if ([...this.selectedOptions].length > 2) {
        alert("Só pode escolher no máximo 2 disciplinas!");
        this.selectedOptions[[...this.selectedOptions].length - 1].selected = false;
      }
    });

    document.getElementById("simuladoForm").addEventListener("submit", function(e){
      e.preventDefault();
      // Aqui você pode armazenar os dados em localStorage ou enviar para backend
      window.location.href = "exam.html";
    });

// Login & Register Page
 function toggleForms() {
      document.getElementById("loginForm").classList.toggle("hidden");
      document.getElementById("signupForm").classList.toggle("hidden");
    }