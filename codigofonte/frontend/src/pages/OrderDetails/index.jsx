import React, { useEffect, useState } from 'react';
import './styles.css';
import { useLocation, useNavigate } from 'react-router-dom';
import { api } from '../../services/api';
import Button from '../../components/Button';

const OrderDetails = () => {
    const { state } = useLocation();
    const navigate = useNavigate();
    const orderId = state && state.orderId;
    const [order, setOrder] = useState(undefined);

    useEffect(() => {
        api.get(`/orders/${orderId}`)
            .then(response => {
                setOrder(response.data)
            })
            .catch(error => console.error('Erro ao buscar pedidos:', error));
    }, [])
    return (
        <div className="container">
            {Boolean(order) ? (<>
                <div className='title-container'>
                    <h1>Detalhes do Pedido</h1>
                    <Button title='Voltar' onClick={() => navigate(-1)} />
                </div>
                <div className="order-details">
                    <p><strong>ID do Cliente:</strong> {order.customer_id}</p>
                    <p><strong>Método de Pagamento:</strong> {order.payment_method}</p>
                    <p><strong>ID do Produto:</strong> {order.product_id}</p>
                    <p><strong>Quantidade:</strong> {order.quantity}</p>
                    <p><strong>Pedido gerado em:</strong> {order.ordered_at}</p>
                </div>
            </>) : <div style={{ width: '100%', height: '100vh', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>Carregando...</div>}
        </div>
    );
};

export default OrderDetails;