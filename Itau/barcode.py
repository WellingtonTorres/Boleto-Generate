

def mod10(entrance):
    caract_ = entrance[::-1]  # we need read from the right to left
    factor_ = 2  # factor begin from 2
    sum_ = 0
    for pos in range(len(caract_)):
        num_ = int(caract_[pos])
        result_ = num_ * factor_
        if result_ >= 10:
            result_str_ = str(result_)
            result_ = int(result_str_[0]) + int(result_str_[1])
        sum_ += result_
        if factor_ == 2:
            factor_ = 1
        else:
            factor_ = 2
    final_result_ = 10 - (sum_ % 10)
    return str(final_result_)


def mod11(entrance):
    caract_ = entrance[::-1]
    factor_ = 2
    sum_ = 0
    for pos in range(len(caract_)):
        num_ = int(caract_[pos])
        result_ = num_ * factor_
        sum_ += result_
        factor_ += 1
        if factor_ > 9:
            factor_ = 2
    final_result_ = 11 - (sum_ % 11)
    return final_result_

# DAC do nosso número
def dacournumber(agencia, cc, carteira, nossonumero):
    entrance_ = str(agencia + cc + carteira + nossonumero)
    if mod10(entrance_) == '10':
        result_ = '0'
    else:
        result_ = mod10(entrance_)

    return str(result_)

# DAC conta corrente e agencia
def dacagenciacc(agencia, cc):
    entrance_ = str(agencia + cc)
    if mod10(entrance_) == '10':
        result_ = '0'
    else:
        result_ = mod10(entrance_)
    return str(result_)



