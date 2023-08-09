/*
  Warnings:

  - You are about to drop the column `ObjectType` on the `Item` table. All the data in the column will be lost.

*/
-- AlterTable
ALTER TABLE `Item` DROP COLUMN `ObjectType`,
    ADD COLUMN `object_type` ENUM('CURVED_SWORD_1H', 'CURVED_SWORD_2H', 'STRAIGHT_SWORD_1H', 'STRAIGHT_SWORD_2H', 'AXE_1H', 'AXE_2H', 'HAMMER_1H', 'HAMMER_2H', 'SPEAR_1H', 'SPEAR_2H', 'JAVELIN_1H', 'STAFF_1H', 'STAFF_2H', 'BOW_2H', 'CROSSBOW_2H', 'DAGGER_1H', 'SMALL_SHIELD', 'MEDIUM_SHIELD', 'LARGE_SHIELD', 'LIGHT_ARMOR', 'MEDIUM_ARMOR', 'HEAVY_ARMOR', 'AMULET', 'TRINKET', 'RING', 'CONSUMABLE', 'MATERIAL', 'KEY', 'OTHER') NOT NULL DEFAULT 'OTHER';
