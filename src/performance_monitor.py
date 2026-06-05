# ==========================================
# MONITORAMENTO DE DESEMPENHO
# ==========================================

import time
import tracemalloc


class PerformanceMonitor:

    @staticmethod
    def medir(funcao, *args, **kwargs):

        tracemalloc.start()

        inicio = time.perf_counter()

        resultado = funcao(
            *args,
            **kwargs
        )

        fim = time.perf_counter()

        memoria_atual, memoria_pico = (
            tracemalloc.get_traced_memory()
        )

        tracemalloc.stop()

        tempo_ms = (
            fim - inicio
        ) * 1000

        memoria_mb = (
            memoria_pico / 1024 / 1024
        )

        return {
            "resultado": resultado,
            "tempo_ms": tempo_ms,
            "memoria_mb": memoria_mb
        }
    
    @staticmethod
    def exibir(nome_algoritmo, dados):

        print("\n========================")
        print(nome_algoritmo)
        print("========================")

        print(
            f"Tempo: {dados['tempo_ms']:.4f} ms"
        )

        print(
            f"Memória: {dados['memoria_mb']:.6f} MB"
        )