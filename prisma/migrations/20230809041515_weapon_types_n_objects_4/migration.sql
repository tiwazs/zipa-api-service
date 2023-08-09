/*
  Warnings:

  - You are about to drop the column `ammo` on the `UnitSpecialization` table. All the data in the column will be lost.
  - You are about to drop the column `shield` on the `UnitSpecialization` table. All the data in the column will be lost.

*/
-- AlterTable
ALTER TABLE `UnitSpecialization` DROP COLUMN `ammo`,
    DROP COLUMN `shield`;
