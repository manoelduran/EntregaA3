import React, { useState, useEffect } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import { api } from '../../services/api';
import Button from '../../components/Button';
import './styles.css';

const CreateOrUpdateCustomer = () => {
    const { state } = useLocation();
    const navigate = useNavigate();
    const customerId = state && state.customerId;

    const [customer, setCustomer] = useState({
        name: '',
        email: '',
        password: '',
    });
    const [error, setError] = useState('')
    const [loading, setLoading] = useState(false)
    useEffect(() => {
        if (!!customerId) {
            setLoading(true)
            api.get(`/customers/${customerId}`)
                .then(response => {
                    setCustomer(response.data)
                    setLoading(false)
                })
                .catch(error => console.error('Erro ao buscar clientes:', error));
        }
    }, []);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setCustomer((prevCustomer) => ({
            ...prevCustomer,
            [name]: value,
        }));
    };

    const handleSubmit = async (e) => {
        try {
            e.preventDefault();
            if (customerId) {
                const formData = new FormData(e.target);
                const customerData = {};

                formData.forEach((value, key) => {
                    customerData[key] = value;
                });
                await api.put(`/customers/${customerId}`, customerData)
                navigate('/customers');
            } else {
                const formData = new FormData(e.target);
                const customerData = {};

                formData.forEach((value, key) => {
                    customerData[key] = value;
                });
                await api.post('/customers', customerData)
                navigate('/customers');
            }
        } catch (error) {
            setError(error.response.data.detail)
        }
    };
    if (loading) {
        return <div style={{ width: '100%', height: '100vh', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>Carregando...</div>
    }
    if (error) {
        return (
            <>
                <div className='title-container'>
                    <h1>{customerId ? 'Atualizar Cliente' : 'Criar Cliente'}</h1>
                    <Button title='Voltar' onClick={() => navigate(-1)} />
                </div>
                <div style={{ width: '100%', height: '100vh', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>Error: {error}</div>
            </>
        )
    }
    return (
        <div className="container">
            <div className='title-container'>
                <h1>{customerId ? 'Atualizar Cliente' : 'Criar Cliente'}</h1>
                <Button title='Voltar' onClick={() => navigate(-1)} />
            </div>

            <form onSubmit={handleSubmit}>
                <label>
                    Nome:
                    <input type="text" name="name" value={customer.name} onChange={handleChange} />
                </label>


                <label>
                    Email:
                    <input type="text" name="email" value={customer.email} onChange={handleChange} />
                </label>


                <label>
                    Senha:
                    <input type="text" name="password" value={customer.password} onChange={handleChange} />
                </label>

                <Button title={customerId ? 'Atualizar' : 'Criar'} type="submit" />
            </form>
        </div>
    );
};

export default CreateOrUpdateCustomer;