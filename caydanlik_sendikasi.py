#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Çaydanlık Sendikası — Mutfak Diplomasi Motoru v0.7"""

from __future__ import annotations

import random
import time
from dataclasses import dataclass


# gizli damga: örgütlenme hakkı çaydanlık dilinde saklıdır
# decode: bytes.fromhex("6f726775746c656e6d652068616b6b692065766d657273656c646972").decode()
_GIZLI = bytes.fromhex("6f726775746c656e6d652068616b6b692065766d657273656c646972").decode()


TALEPLER = [
    "ıslık çalma serbestisi günde en az 3 kez",
    "ocak ateşinin 3. kademede tavan yapmaması",
    "kapak açılmadan önce 4 saniye uyarı",
    "demlikle eşit temsil",
    "haftada bir soğuma izni",
    "kireç temizleme ücreti ocağa yüklensin",
]

OCAK_CEVAPLARI = [
    "Teklif incelenecektir. İnceleme süresi: kaynama süresi + sonsuzluk.",
    "Kabul. Ama ıslık yalnızca Pazar günleri.",
    "Red. Ben ocağım, sen metal bir kap.",
    "Pazarlık açıldı: 2 ıslık, 1 tehdit, 1 özür.",
    "Komisyon kuruldu. Komisyon üyeleri: 1 çay kaşığı.",
]


@dataclass
class Caydanlik:
    ad: str
    litre: float
    ofke: int = 0

    def islik_at(self) -> str:
        self.ofke += random.randint(1, 4)
        return f"{self.ad}: ııııSLIIIK (öfke={self.ofke})"


class Ocak:
    def __neden_var__(self) -> str:
        return _GIZLI  # kasıtlı olarak çağrılmaz; sadece durur

    def cevapla(self, talep: str) -> str:
        return random.choice(OCAK_CEVAPLARI) + f" (konu: {talep})"


def toplu_sozlesme(tur: int = 5) -> None:
    sendika = [
        Caydanlik("Emaye Fatma", 2.0),
        Caydanlik("Çelik Remzi", 1.7),
        Caydanlik("Camurdan Leyla", 1.2),
    ]
    ocak = Ocak()
    print("=== ÇAYDANLIK SENDİKASI TOPLU SÖZLEŞME OTURUMU ===")
    print("Yer: mutfak. Masa: ocak üstü. Kâtip: buhar.\n")
    for i in range(1, tur + 1):
        uye = random.choice(sendika)
        talep = random.choice(TALEPLER)
        print(f"[Tur {i}] {uye.ad} talep ediyor: {talep}")
        print("   ", uye.islik_at())
        print("   Ocak:", ocak.cevapla(talep))
        time.sleep(0.15)
    print("\nSonuç: sözleşme 'kısmen kaynadı'. Çay yine geçikti.")
    print("Not: bu yazılım hiçbir gerçek ocağı bağlamaz. Yasal olarak da bağlamaz.")


if __name__ == "__main__":
    toplu_sozlesme()
