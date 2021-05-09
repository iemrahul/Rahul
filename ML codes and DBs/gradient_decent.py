import numpy as np

def gradient_descent(x,y):
    m_curr = b_curr =0
    iterations=10000
    n=len(x)
    learning_rate = 0.08
    for i in range(iterations):
        y_predicted = m_curr * x + b_curr
        # Mean Squared Error
        mean_squared_error = sum([x**2 for x in (y-y_predicted)])/n
        # Derivative Of m and b
        m_der = -(2/n)*(sum(x*(y-y_predicted)))
        b_der = -(2/n)*(sum(y-y_predicted))

        m_curr = m_curr - learning_rate * m_der
        b_curr = b_curr - learning_rate * b_der
        print('m {}, b {} , cost {}'.format(m_curr,b_curr,mean_squared_error))


X = np.array([1,2,3,4,5])
Y = np.array([5,7,9,11,13])
gradient_descent(X,Y)