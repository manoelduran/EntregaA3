import React, { useState, useEffect } from 'react';
import Button from '../../components/Button'
import './styles.css';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';


const CustomersDashboard = () => {
    const navigate = useNavigate();
    const [customers, setCustomers] = useState([
        {
            id: 1,
            name: 'Alice Oliveira',
            email: 'alice@email.com',
            password: 'senha123',
            created_at: '2023-01-01T12:00:00',
        },
        {
            id: 2,
            name: 'Bob Silva',
            email: 'bob@email.com',
            password: 'senha456',
            created_at: '2023-02-01T14:30:00',
        },
        {
            id: 3,
            name: 'Carlos Pereira',
            email: 'carlos@email.com',
            password: 'senha789',
            created_at: '2023-03-05T08:45:00',
        },
        {
            id: 4,
            name: 'Danielle Santos',
            email: 'danielle@email.com',
            password: 'senhaABC',
            created_at: '2023-04-10T17:20:00',
        },
        {
            id: 5,
            name: 'Eduardo Lima',
            email: 'eduardo@email.com',
            password: 'senhaDEF',
            created_at: '2023-05-15T09:30:00',
        },
        {
            id: 6,
            name: 'Fernanda Costa',
            email: 'fernanda@email.com',
            password: 'senhaGHI',
            created_at: '2023-06-20T14:15:00',
        },
        {
            id: 7,
            name: 'Gabriel Sousa',
            email: 'gabriel@email.com',
            password: 'senhaJKL',
            created_at: '2023-07-25T11:45:00',
        },
        {
            id: 8,
            name: 'Helena Pereira',
            email: 'helena@email.com',
            password: 'senhaMNO',
            created_at: '2023-08-30T13:00:00',
        },
        {
            id: 9,
            name: 'Isaac Silva',
            email: 'isaac@email.com',
            password: 'senhaPQR',
            created_at: '2023-09-05T16:30:00',
        },
        {
            id: 10,
            name: 'Julia Oliveira',
            email: 'julia@email.com',
            password: 'senhaSTU',
            created_at: '2023-10-10T10:00:00',
        },
    ]);

    useEffect(() => {
        // Substitua a URL abaixo pela sua API ou endpoint para buscar os clientes
        axios.get('sua-api-aqui/customers')
            .then(response => setCustomers(response.data))
            .catch(error => console.error('Erro ao buscar clientes:', error));
    }, []);
    const handleView = (customerId) => {
        // Lógica para visualizar o customer com o ID fornecido
        console.log(`Visualizar customer com ID ${customerId}`);
    };

    const handleDelete = (customerId) => {
        // Lógica para deletar o customer com o ID fornecido
        console.log(`Deletar customer com ID ${customerId}`);
    };

    const handleUpdate = (customerId) => {
        // Lógica para atualizar o customer com o ID fornecido
        console.log(`Atualizar customer com ID ${customerId}`);
    };
    return (
        <div className="table-container">
            <div className="table-header">
                <h2 className="table-title">Lista de Clientes</h2>
                <div className="table-actions">
                    <Button onClick={() => { }} title="Criar Cliente" color="#808080" />
                    <Button onClick={() => navigate('/')} title="Voltar" color="#808080" />
                </div>
            </div>
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Nome</th>
                        <th>E-mail</th>
                        <th>Senha</th>
                        <th>Data de Criação</th>
                        <th>Ações</th>
                    </tr>
                </thead>
                <tbody>
                    {customers.map(customer => (
                        <tr key={customer.id}>
                            <td>{customer.id}</td>
                            <td>{customer.name}</td>
                            <td>{customer.email}</td>
                            <td>{customer.password}</td>
                            <td>{customer.created_at}</td>
                            <td>
                                <Button onClick={() => handleView(customer.id)} title="Visualizar" color="#007BFF" />
                                <Button onClick={() => handleDelete(customer.id)} title="Deletar" color="#DC3545" />
                                <Button onClick={() => handleUpdate(customer.id)} title="Atualizar" color="#4CAF50" />
                                <Button onClick={() => handleUpdate(customer.id)} title="Histórico de Pedidos" color="#FFA500" />
                                <Button onClick={() => handleUpdate(customer.id)} title="Consumo Médio" color="#FFA500" />
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default CustomersDashboard;
