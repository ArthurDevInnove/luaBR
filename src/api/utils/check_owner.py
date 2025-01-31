from fastapi import HTTPException, status

def check_owner(first_id: int, second_id: int):
    if first_id != second_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Você não tem permissão para isso.'
        )