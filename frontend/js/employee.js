const token = localStorage.getItem('access_token');
if (!token) {
  window.location.href = '404.html';
} else {
  const apiUrl = 'http://localhost:5000/api/employees';

  let editId = null;

  async function fetchEmployees() {
    const res = await fetch(apiUrl);
    const employees = await res.json();

    const tbody = document.getElementById('employeeTableBody');
    tbody.innerHTML = '';

    employees.forEach(emp => {
      const tr = document.createElement('tr');
      tr.innerHTML = `
        <td class="p-3">${emp.id}</td>
        <td class="p-3">${emp.full_name}</td>
        <td class="p-3">${emp.email}</td>
        <td class="p-3">${emp.phone || ''}</td>
        <td class="p-3">
          <button onclick="deleteEmployee(${emp.id})" class="text-red-500 hover:underline mr-2">Supprimer</button>
          <button onclick="editEmployee(${emp.id})" class="text-blue-500 hover:underline">Modifier</button>
        </td>
      `;
      tbody.appendChild(tr);
    });
  }
window.deleteEmployee = async function(id){

    if (!confirm('Voulez-vous vraiment supprimer cet employé ?')) return;

    await fetch(`${apiUrl}/${id}`, { method: 'DELETE' });
    fetchEmployees();
  }
window.editEmployee = async function(id){

    const res = await fetch(`${apiUrl}/${id}`);
    if (!res.ok) {
      alert('Erreur lors de la récupération de l\'employé');
      return;
    }
    const emp = await res.json();

    document.getElementById('full_name').value = emp.full_name || '';
    document.getElementById('email').value = emp.email || '';
    document.getElementById('phone').value = emp.phone || '';
    document.getElementById('hire_date').value = emp.hire_date || '';
    document.getElementById('department_id').value = emp.department_id || '';
    document.getElementById('position_id').value = emp.position_id || '';

    editId = id;
    document.querySelector('#employeeForm button[type="submit"]').textContent = 'Modifier';
  }

  document.getElementById('employeeForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const employeeData = {
      full_name: document.getElementById('full_name').value,
      email: document.getElementById('email').value,
      phone: document.getElementById('phone').value,
      hire_date: document.getElementById('hire_date').value,
      department_id: Number(document.getElementById('department_id').value),
      position_id: Number(document.getElementById('position_id').value),
    };

    let response;
    if (editId) {
      response = await fetch(`${apiUrl}/${editId}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(employeeData),
      });
    } else {
      response = await fetch(apiUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(employeeData),
      });
    }

    if (!response.ok) {
      alert('Erreur lors de la sauvegarde');
      return;
    }

    e.target.reset();
    editId = null;
    document.querySelector('#employeeForm button[type="submit"]').textContent = 'Ajouter';

    fetchEmployees();
  });

  fetchEmployees();
}
