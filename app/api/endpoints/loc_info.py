from fastapi import APIRouter, HTTPException
from app.service.loc_info import *
from app.schemas.loc_info import *
from fastapi import Request


router = APIRouter()



@router.post("/select_loc_info")
async def filter_data(filters: FilterRequest):
    # 입력된 값만 딕셔너리로 변환 (unset된 필드는 제외)
    filters_dict = filters.dict(exclude_unset=True)
    # 필터 데이터를 서비스 레이어로 전달
    result, all_corr_matrix, filter_corr_matrix = await filter_location_info(filters_dict)

    return {"filtered_data": result, "all_corr" : all_corr_matrix, "filter_corr" : filter_corr_matrix}