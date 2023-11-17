import React, { useState, useEffect } from 'react';
import Button from '../../components/Button'
import './styles.css';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
const OrdersDashboard = () => {
    const navigate = useNavigate();
    const [orders, setOrders] = useState([
        {
            id: 1,
            customer_id: 1,
            payment_method: 'Credit Card',
            product_id: 1,
            quantity: 2,
            ordered_at: '2023-01-01T14:00:00',
        },
        {
            id: 2,
            customer_id: 2,
            payment_method: 'PayPal',
            product_id: 3,
            quantity: 1,
            ordered_at: '2023-02-03T10:30:00',
        },
        {
            id: 3,
            customer_id: 3,
            payment_method: 'Cash',
            product_id: 2,
            quantity: 3,
            ordered_at: '2023-03-05T12:45:00',
        },
        {
            id: 4,
            customer_id: 4,
            payment_method: 'Credit Card',
            product_id: 4,
            quantity: 2,
            ordered_at: '2023-04-10T16:20:00',
        },
        {
            id: 5,
            customer_id: 5,
            payment_method: 'PayPal',
            product_id: 5,
            quantity: 1,
            ordered_at: '2023-05-15T08:30:00',
        },
        {
            id: 6,
            customer_id: 6,
            payment_method: 'Cash',
            product_id: 6,
            quantity: 2,
            ordered_at: '2023-06-20T13:15:00',
        },
        {
            id: 7,
            customer_id: 7,
            payment_method: 'Credit Card',
            product_id: 7,
            quantity: 3,
            ordered_at: '2023-07-25T10:45:00',
        },
        {
            id: 8,
            customer_id: 8,
            payment_method: 'PayPal',
            product_id: 8,
            quantity: 1,
            ordered_at: '2023-08-30T12:00:00',
        },
        {
            id: 9,
            customer_id: 9,
            payment_method: 'Cash',
            product_id: 9,
            quantity: 4,
            ordered_at: '2023-09-05T15:30:00',
        },
        {
            id: 10,
            customer_id: 10,
            payment_method: 'Credit Card',
            product_id: 10,
            quantity: 2,
            ordered_at: '2023-10-10T09:00:00',
        },
    ]);

    useEffect(() => {
        // Substitua a URL abaixo pela sua API ou endpoint para buscar os clientes
        axios.get('sua-api-aqui/customers')
            .then(response => setOrders(response.data))
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
                <h2 className="table-title">Lista de Pedidos</h2>
                <div className="table-actions">
                    <Button onClick={() => { }} title="Criar Pedido" color="#808080" />
                    <Button onClick={() => navigate('/')} title="Voltar" color="#808080" />
                </div>
            </div>
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>ID do Customer</th>
                        <th>Método de Pagamento</th>
                        <th>ID do Produto</th>
                        <th>Quantidade</th>
                        <th>Dia da Criação do Pedido</th>
                        <th>Ações</th>
                    </tr>
                </thead>
                <tbody>
                    {orders.map(order => (
                        <tr key={order.id}>
                            <td>{order.id}</td>
                            <td>{order.customer_id}</td>
                            <td>{order.payment_method}</td>
                            <td>{order.product_id}</td>
                            <td>{order.quantity}</td>
                            <td>{order.ordered_at}</td>
                            <td>
                                <Button onClick={() => handleView(order.id)} title="Visualizar" color="#007BFF" />
                                <Button onClick={() => handleDelete(order.id)} title="Deletar" color="#DC3545" />
                                <Button onClick={() => handleUpdate(order.id)} title="Atualizar" color="#4CAF50" />
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default OrdersDashboard;
