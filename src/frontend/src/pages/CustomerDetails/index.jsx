import React, { useEffect, useState } from 'react';
import './styles.css';
import { useLocation, useNavigate } from 'react-router-dom';
import { api } from '../../services/api';
import Button from '../../components/Button';

const CustomerDetails = () => {
    const { state } = useLocation();
    const navigate = useNavigate();
    const customerId = state && state.customerId;
    const [customer, setCustomer] = useState(undefined)
    useEffect(() => {
        api.get(`/customers/${customerId}`)
            .then(response => {
                setCustomer(response.data)

            })
            .catch(error => console.error('Erro ao buscar clientes:', error));
    }, [])
    return (
        <div className="container">
            {Boolean(customer) ? (<>
                <div className='title-container'>
                    <h1>Detalhes do Cliente</h1>
                    <Button title='Voltar' onClick={() => navigate(-1)} />
                </div>
                <div className="customer-details">
                    <p><strong>Nome:</strong> {customer.name}</p>
                    <p><strong>Email:</strong> {customer.email}</p>
                    <p><strong>Criado em:</strong> {customer.created_at}</p>
                </div>
            </>) : <div style={{ width: '100%', height: '100vh', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>Carregando...</div>}
        </div>
    );
};

export default CustomerDetails;