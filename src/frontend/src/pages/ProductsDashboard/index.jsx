import React, { useState, useEffect } from 'react';
import Button from '../../components/Button';
import './styles.css';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';


const ProductsDashboard = () => {
    const navigate = useNavigate();
    const [products, setProducts] = useState([
        {
            id: 1,
            name: 'Product A',
            price: 50,
            quantity: 100,
            created_at: '2023-01-01T12:00:00',
        },
        {
            id: 2,
            name: 'Product B',
            price: 30,
            quantity: 80,
            created_at: '2023-02-01T14:30:00',
        },
        {
            id: 3,
            name: 'Product C',
            price: 25,
            quantity: 120,
            created_at: '2023-03-05T08:45:00',
        },
        {
            id: 4,
            name: 'Product D',
            price: 40,
            quantity: 90,
            created_at: '2023-04-10T17:20:00',
        },
        {
            id: 5,
            name: 'Product E',
            price: 60,
            quantity: 60,
            created_at: '2023-05-15T09:30:00',
        },
        {
            id: 6,
            name: 'Product F',
            price: 35,
            quantity: 150,
            created_at: '2023-06-20T14:15:00',
        },
        {
            id: 7,
            name: 'Product G',
            price: 55,
            quantity: 110,
            created_at: '2023-07-25T11:45:00',
        },
        {
            id: 8,
            name: 'Product H',
            price: 70,
            quantity: 75,
            created_at: '2023-08-30T13:00:00',
        },
        {
            id: 9,
            name: 'Product I',
            price: 45,
            quantity: 100,
            created_at: '2023-09-05T16:30:00',
        },
        {
            id: 10,
            name: 'Product J',
            price: 50,
            quantity: 120,
            created_at: '2023-10-10T10:00:00',
        },
    ]);

    useEffect(() => {
        // Substitua a URL abaixo pela sua API ou endpoint para buscar os clientes
        axios.get('sua-api-aqui/customers')
            .then(response => setProducts(response.data))
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
                <h2 className="table-title">Lista de Produtos</h2>
            <div className="table-actions">
            <Button onClick={() => { }} title="Criar Produto" color="#808080" />
                <Button onClick={() => { }} title="Mais Vendidos" color="#808080" />
                <Button onClick={() => { }} title="Estoque Baixo" color="#FF69B4" />
                <Button onClick={() => navigate('/')} title="Voltar" color="#808080" />
            </div>
            </div>
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Nome</th>
                        <th>Preço</th>
                        <th>Quantidade</th>
                        <th>Data de Criação</th>
                        <th>Ações</th>
                    </tr>
                </thead>
                <tbody>
                    {products.map(product => (
                        <tr key={product.id}>
                            <td>{product.id}</td>
                            <td>{product.name}</td>
                            <td>{product.price}</td>
                            <td>{product.quantity}</td>
                            <td>{product.created_at}</td>
                            <td>
                                <Button onClick={() => handleView(product.id)} title="Visualizar" color="#007BFF" />
                                <Button onClick={() => handleDelete(product.id)} title="Deletar" color="#DC3545" />
                                <Button onClick={() => handleUpdate(product.id)} title="Atualizar" color="#4CAF50" />
                                <Button onClick={() => handleUpdate(product.id)} title="Histórico de Venda" color="#FFA500" />
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default ProductsDashboard;
