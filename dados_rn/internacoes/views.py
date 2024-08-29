from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .db_connection import db
from rest_framework import viewsets
from bson import ObjectId

internacoes_collection = db['internacoes_collection']
leitos_collection = db['leitos_collection']


class MediaDiasInternacaoPorEspecialidade(APIView):
    def get(self, request, *args, **kwargs):
        especialidade = request.query_params.get('especialidade', None)
        cnes = request.query_params.get('cnes', None)
        mes_ano_inicio = request.query_params.get('mes_ano_inicio', None)
        mes_ano_fim = request.query_params.get('mes_ano_fim', None)
        municipio_res = request.query_params.get('municipio_res', None)
        municipio_mov = request.query_params.get('municipio_mov', None)
        
        match_stage = {}

        if especialidade:
            match_stage['ESPEC'] = int(especialidade)
        
        if cnes:
            match_stage['CNES'] = int(cnes)
        
        if mes_ano_inicio and mes_ano_fim:
            match_stage['DT_INTER'] = {
                "$gte": int(mes_ano_inicio + "01"),
                "$lte": int(mes_ano_fim + "31")
            }
        
        if municipio_res:
            match_stage['MUNIC_RES'] = int(municipio_res)
        
        if municipio_mov:
            match_stage['MUNIC_MOV'] = int(municipio_mov)
        
        pipeline = [
            {"$match": match_stage} if match_stage else {},
            {"$group": {
                "_id": "$ESPEC",
                "media_dias_internacao": {"$avg": "$DIAS_PERM"}
            }}
        ]

        pipeline = [stage for stage in pipeline if stage]

        try:
            result = list(internacoes_collection.aggregate(pipeline))
            return Response(result, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class NumeroPercentualInternacoesPorCausa(APIView):
    def get(self, request):
        capitulo_cid = request.query_params.get('capitulo_cid')
        cnes = request.query_params.get('cnes', None)
        mes_ano_inicio = request.query_params.get('mes_ano_inicio', None)
        mes_ano_fim = request.query_params.get('mes_ano_fim', None)
        municipio_res = request.query_params.get('municipio_res', None)
        municipio_mov = request.query_params.get('municipio_mov', None)
        
        match_stage = {}

        if capitulo_cid:
            match_stage['DIAG_PRINC'] = {"$regex": f"^{capitulo_cid}"}
        
        if cnes:
            match_stage['CNES'] = int(cnes)
        
        if mes_ano_inicio and mes_ano_fim:
            match_stage['DT_INTER'] = {
                "$gte": int(mes_ano_inicio + "01"),
                "$lte": int(mes_ano_fim + "31")
            }
        
        if municipio_res:
            match_stage['MUNIC_RES'] = int(municipio_res)
        
        if municipio_mov:
            match_stage['MUNIC_MOV'] = int(municipio_mov)

        pipeline = [
            {"$match": match_stage} if match_stage else {},
            {"$group": {
                "_id": "$DIAG_PRINC",
                "numero_internacoes": {"$sum": 1}
            }},
            {"$group": {
                "_id": None,
                "total_internacoes": {"$sum": "$numero_internacoes"},
                "detalhes": {"$push": {"_id": "$_id", "numero_internacoes": "$numero_internacoes"}}
            }},
            {"$unwind": "$detalhes"},
            {"$project": {
                "_id": 0,
                "capitulo_cid": "$detalhes._id",
                "numero_internacoes": "$detalhes.numero_internacoes",
                "percentual_internacoes": {"$multiply": [{"$divide": ["$detalhes.numero_internacoes", "$total_internacoes"]}, 100]}
            }}
        ]

        pipeline = [stage for stage in pipeline if stage]

        try:
            result = list(internacoes_collection.aggregate(pipeline))
            return Response(result, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ValorMedioInternacaoPorEspecialidade(APIView):
    def get(self, request):
        especialidade = request.query_params.get('especialidade')
        cnes = request.query_params.get('cnes', None)
        mes_ano_inicio = request.query_params.get('mes_ano_inicio', None)
        mes_ano_fim = request.query_params.get('mes_ano_fim', None)
        municipio_res = request.query_params.get('municipio_res', None)
        municipio_mov = request.query_params.get('municipio_mov', None)
        
        match_stage = {}

        if especialidade:
            match_stage['ESPEC'] = int(especialidade)
        
        if cnes:
            match_stage['CNES'] = int(cnes)
        
        if mes_ano_inicio and mes_ano_fim:
            match_stage['DT_INTER'] = {
                "$gte": int(mes_ano_inicio + "01"),
                "$lte": int(mes_ano_fim + "31")
            }
        
        if municipio_res:
            match_stage['MUNIC_RES'] = int(municipio_res)
        
        if municipio_mov:
            match_stage['MUNIC_MOV'] = int(municipio_mov)

        pipeline = [
            {"$match": match_stage} if match_stage else {},
            {"$group": {
                "_id": "$ESPEC",
                "valor_medio": {"$avg": "$VAL_TOT"}
            }}
        ]

        pipeline = [stage for stage in pipeline if stage]

        try:
            result = list(internacoes_collection.aggregate(pipeline))
            return Response(result, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class TaxaOcupacaoHospitalarPorEstabelecimento(APIView):
    def get(self, request):
        cnes = request.query_params.get('cnes', None)
        mes_ano_inicio = request.query_params.get('mes_ano_inicio', None)
        mes_ano_fim = request.query_params.get('mes_ano_fim', None)
        municipio_res = request.query_params.get('municipio_res', None)
        municipio_mov = request.query_params.get('municipio_mov', None)
        
        match_stage_internacoes = {}

        if cnes:
            match_stage_internacoes['CNES'] = int(cnes)
        
        if mes_ano_inicio and mes_ano_fim:
            match_stage_internacoes['DT_INTER'] = {
                "$gte": int(mes_ano_inicio + "01"),  # Adicionando dia 01 para início do mês
                "$lte": int(mes_ano_fim + "31")  # Adicionando dia 31 para final do mês
            }
        
        if municipio_res:
            match_stage_internacoes['MUNIC_RES'] = int(municipio_res)
        
        if municipio_mov:
            match_stage_internacoes['MUNIC_MOV'] = int(municipio_mov)

        pipeline_internacoes = [
            {"$match": match_stage_internacoes} if match_stage_internacoes else {},
            {"$group": {
                "_id": "$CNES",
                "total_internacoes": {"$sum": 1}
            }}
        ]
        
        match_stage_leitos = {"TP_LEITO": {"$ne": 7}}

        pipeline_leitos = [
            {"$match": match_stage_leitos},
            {"$group": {
                "_id": "$CNES",
                "total_leitos": {"$sum": "$QT_SUS"}
            }}
        ]
        
        try:
            internacoes = list(internacoes_collection.aggregate([stage for stage in pipeline_internacoes if stage]))
            leitos = list(leitos_collection.aggregate(pipeline_leitos))
            
            leitos_dict = {item['_id']: item['total_leitos'] for item in leitos}
            
            result = []
            for item in internacoes:
                cnes = item['_id']
                total_internacoes = item['total_internacoes']
                total_leitos = leitos_dict.get(cnes, 0)
                taxa_ocupacao = (total_internacoes / (total_leitos * 30)) * 100 if total_leitos > 0 else 0
                
                result.append({
                    "cnes": cnes,
                    "total_internacoes": total_internacoes,
                    "total_leitos": total_leitos,
                    "taxa_ocupacao": taxa_ocupacao
                })
            
            return Response(result, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

