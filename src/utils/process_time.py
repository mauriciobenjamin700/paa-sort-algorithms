from datetime import datetime


def process_time_diference_in_ms(start: datetime, end: datetime) -> float:
    """Calcula a diferença de tempo entre start e end em milissegundos."""
    return (end - start).total_seconds() * 1000
