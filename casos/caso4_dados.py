"""Gera caso4_cenarios.db: 12 cenários do reator resolvidos pelo modelo do caso 1."""
import sqlite3
from pathlib import Path

import caso_reator as c

CENARIOS = [
    ("2026-11-03", "ana",   5000, 500), ("2026-11-04", "ana",   4500, 500),
    ("2026-11-05", "ana",   5000, 700), ("2026-11-06", "ana",   2600, 500),
    ("2026-11-03", "bruno", 5000, 500), ("2026-11-05", "bruno", 5500, 500),
    ("2026-11-07", "bruno", 5000, 100), ("2026-11-10", "bruno", 6000, 450),
    ("2026-11-04", "carla", 4000, 600), ("2026-11-06", "carla", 5000, 500),
    ("2026-11-09", "carla", 3000, 800), ("2026-11-11", "carla", 4800, 520),
]

SCHEMA = """
CREATE TABLE cenarios (
    id            INTEGER PRIMARY KEY,
    criado_em     DATE    NOT NULL,
    analista      TEXT    NOT NULL,
    preco_p       NUMERIC NOT NULL,
    disp_a        NUMERIC NOT NULL,
    status        TEXT    NOT NULL,
    margem        NUMERIC
);
CREATE TABLE producao (
    cenario_id    INTEGER NOT NULL REFERENCES cenarios(id),
    produto       TEXT    NOT NULL,
    toneladas     NUMERIC NOT NULL,
    PRIMARY KEY (cenario_id, produto)
);
"""


def gerar(destino: Path):
    destino.unlink(missing_ok=True)
    con = sqlite3.connect(destino)
    con.executescript(SCHEMA)
    for i, (data, analista, preco_p, disp_a) in enumerate(CENARIOS, start=1):
        if disp_a * 1.0 < 200 * c.cons["Q"]["A"]:
            con.execute("INSERT INTO cenarios VALUES (?,?,?,?,?,?,?)", (i, data, analista, preco_p, disp_a, "infeasible", None))
            continue
        original = c.disp["A"]
        c.disp["A"] = disp_a
        r = c.resolver(pv_P=preco_p)
        c.disp["A"] = original
        con.execute("INSERT INTO cenarios VALUES (?,?,?,?,?,?,?)", (i, data, analista, preco_p, disp_a, "optimal", r["margem"]))
        for produto in ("P", "Q"):
            if r[produto] > 0.05:
                con.execute("INSERT INTO producao VALUES (?,?,?)", (i, produto, r[produto]))
    con.commit()
    con.close()


if __name__ == "__main__":
    gerar(Path(__file__).with_name("caso4_cenarios.db"))
    print("caso4_cenarios.db gerado")
